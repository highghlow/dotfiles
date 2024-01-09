require("mason").setup()
require("barbar").setup()
require("gitui").setup()
require('deferred-clipboard').setup {
  fallback = 'unnamedplus'
}
vim.api.nvim_create_autocmd(
	'vimEnter',
	{
		command='Neotree'
	}
)

local lsp = require("lspconfig")

vim.g.coq_settings = { auto_start='shut-up' }
local coq = require("coq")

lsp.pyright.setup(coq.lsp_ensure_capabilities({}))
lsp.taplo.setup(coq.lsp_ensure_capabilities({}))
lsp.lua_ls.setup(coq.lsp_ensure_capabilities({}))
lsp.rust_analyzer.setup(coq.lsp_ensure_capabilities({}))
