"""
CampusPrep Supabase Cloud Integration Service
Provides unified access to Supabase Auth, PostgreSQL metrics, JWKS verification, and PostgREST.
"""
import os
import json
import logging
import urllib.request
import urllib.error

logger = logging.getLogger(__name__)

class SupabaseService:
    def __init__(self, url=None, publishable_key=None, secret_key=None, jwks_url=None):
        self.url = (url or os.environ.get('SUPABASE_URL', 'https://tcnktohuqrjzipnfnafw.supabase.co')).rstrip('/')
        self.publishable_key = publishable_key or os.environ.get('SUPABASE_PUBLISHABLE_KEY', 'sb_publishable_wSMMzkt_ado0gXqYPJW6RA_8Uj1FwUb')
        self.secret_key = secret_key or os.environ.get('SUPABASE_SECRET_KEY')
        self.jwks_url = jwks_url or os.environ.get('SUPABASE_JWKS_URL', f"{self.url}/auth/v1/.well-known/jwks.json")
        self._cached_jwks = None

    def get_public_config(self):
        """Returns safe public configuration for client-side JavaScript initialization."""
        return {
            'supabase_url': self.url,
            'publishable_key': self.publishable_key,
            'jwks_url': self.jwks_url,
            'project_ref': self.url.replace('https://', '').split('.')[0] if self.url else ''
        }

    def check_health(self):
        """Checks connectivity to Supabase Auth and JWKS endpoints."""
        status = {
            'healthy': False,
            'url': self.url,
            'auth_service': 'disconnected',
            'jwks_service': 'disconnected',
            'error': None
        }

        # 1. Check JWKS endpoint
        try:
            req = urllib.request.Request(self.jwks_url, headers={'User-Agent': 'CampusPrep-Server/1.0'})
            with urllib.request.urlopen(req, timeout=5) as resp:
                if resp.status == 200:
                    status['jwks_service'] = 'connected'
                    self._cached_jwks = json.loads(resp.read().decode('utf-8'))
        except Exception as e:
            status['jwks_service'] = f"failed: {str(e)}"

        # 2. Check Auth service health
        try:
            auth_health_url = f"{self.url}/auth/v1/health"
            req = urllib.request.Request(
                auth_health_url,
                headers={
                    'apikey': self.publishable_key,
                    'User-Agent': 'CampusPrep-Server/1.0'
                }
            )
            with urllib.request.urlopen(req, timeout=5) as resp:
                if resp.status == 200:
                    status['auth_service'] = 'connected'
        except Exception as e:
            status['auth_service'] = f"failed: {str(e)}"

        status['healthy'] = (status['jwks_service'] == 'connected' and status['auth_service'] == 'connected')
        return status

    def get_jwks(self, force_refresh=False):
        """Retrieves and caches the JSON Web Key Set from Supabase."""
        if self._cached_jwks and not force_refresh:
            return self._cached_jwks

        try:
            req = urllib.request.Request(self.jwks_url, headers={'User-Agent': 'CampusPrep-Server/1.0'})
            with urllib.request.urlopen(req, timeout=5) as resp:
                self._cached_jwks = json.loads(resp.read().decode('utf-8'))
                return self._cached_jwks
        except Exception as e:
            logger.error("Failed to fetch Supabase JWKS: %s", e)
            return None

    def list_auth_users(self, page=1, per_page=50):
        """Fetches list of registered users from Supabase Auth admin API using Secret Key."""
        url = f"{self.url}/auth/v1/admin/users?page={page}&per_page={per_page}"
        try:
            req = urllib.request.Request(
                url,
                headers={
                    'apikey': self.secret_key,
                    'Authorization': f"Bearer {self.secret_key}",
                    'Content-Type': 'application/json',
                    'User-Agent': 'CampusPrep-Server/1.0'
                }
            )
            with urllib.request.urlopen(req, timeout=6) as resp:
                return json.loads(resp.read().decode('utf-8'))
        except urllib.error.HTTPError as e:
            err_msg = e.read().decode('utf-8', errors='ignore')
            logger.error("Supabase Admin Users API error %d: %s", e.code, err_msg)
            return {'users': [], 'error': f"HTTP {e.code}: {err_msg}"}
        except Exception as e:
            logger.error("Supabase Admin Users API failed: %s", e)
            return {'users': [], 'error': str(e)}

# Singleton instance
supabase_service = SupabaseService()
