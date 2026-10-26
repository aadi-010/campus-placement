/**
 * Lightweight, fast streaming markdown renderer for Gemma 4 output
 * Safely parses markdown constructs with live copy-to-clipboard code blocks.
 */
class MarkdownRenderer {
  static escapeHtml(str) {
    if (!str) return '';
    return str
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#039;');
  }

  /**
   * Separates reasoning / thoughts if wrapped in <thought>...</thought> or <reasoning> tags
   */
  static extractThoughts(rawText) {
    let thought = '';
    let response = rawText;

    const thoughtRegex = /<(?:thought|reasoning|think)>([\s\S]*?)(?:<\/(?:thought|reasoning|think)>|$)/i;
    const match = rawText.match(thoughtRegex);

    if (match) {
      thought = match[1].trim();
      response = rawText.replace(match[0], '').trim();
    }

    return { thought, response };
  }

  static render(text) {
    if (!text) return '';

    // First handle fenced code blocks: ```lang \n code \n ```
    const codeBlocks = [];
    let processed = text.replace(/```([a-zA-Z0-9_\-\+]*)\n([\s\S]*?)```/g, (match, lang, code) => {
      const id = 'code_block_' + Math.random().toString(36).substring(2, 9);
      const language = lang.trim() || 'code';
      const cleanCode = this.escapeHtml(code.trim());
      
      const blockHtml = `
        <div class="code-header-bar">
          <span>${language}</span>
          <button class="code-copy-btn" onclick="navigator.clipboard.writeText(decodeURIComponent('${encodeURIComponent(code.trim())}')); this.innerText='Copied!'; setTimeout(() => this.innerText='Copy', 1500);">Copy</button>
        </div>
        <pre><code class="language-${language}">${cleanCode}</code></pre>
      `;
      codeBlocks.push(blockHtml);
      return `__CODE_BLOCK_${codeBlocks.length - 1}__`;
    });

    // Escape any remaining HTML
    processed = this.escapeHtml(processed);

    // Headings
    processed = processed.replace(/^### (.*$)/gim, '<h3>$1</h3>');
    processed = processed.replace(/^## (.*$)/gim, '<h2>$1</h2>');
    processed = processed.replace(/^# (.*$)/gim, '<h1>$1</h1>');

    // Bold & Italics
    processed = processed.replace(/\*\*\*(.*?)\*\*\*/gim, '<strong><em>$1</em></strong>');
    processed = processed.replace(/\*\*(.*?)\*\*/gim, '<strong>$1</strong>');
    processed = processed.replace(/\*(.*?)\*/gim, '<em>$1</em>');

    // Inline Code
    processed = processed.replace(/`([^`]+)`/g, '<code>$1</code>');

    // Blockquotes
    processed = processed.replace(/^\> (.*$)/gim, '<blockquote>$1</blockquote>');

    // Unordered Lists
    processed = processed.replace(/^\s*[\-\*]\s+(.*)$/gim, '<li>$1</li>');
    processed = processed.replace(/(<li>[\s\S]*?<\/li>)/g, '<ul>$1</ul>');
    processed = processed.replace(/<\/ul>\s*<ul>/g, '');

    // Links [text](url)
    processed = processed.replace(/\[([^\]]+)\]\(([^)]+)\)/g, '<a href="$2" target="_blank" rel="noopener noreferrer">$1</a>');

    // Line breaks to paragraphs
    const paragraphs = processed.split(/\n\n+/);
    processed = paragraphs.map(p => {
      p = p.trim();
      if (!p) return '';
      if (p.startsWith('<h1>') || p.startsWith('<h2>') || p.startsWith('<h3>') ||
          p.startsWith('<ul>') || p.startsWith('<pre>') || p.startsWith('<blockquote>') ||
          p.startsWith('__CODE_BLOCK_')) {
        return p;
      }
      return `<p>${p.replace(/\n/g, '<br>')}</p>`;
    }).join('\n');

    // Restore Code Blocks
    codeBlocks.forEach((block, index) => {
      processed = processed.replace(`__CODE_BLOCK_${index}__`, block);
    });

    return processed;
  }
}

window.MarkdownRenderer = MarkdownRenderer;
