require("mason").setup()
require("barbar").setup()
require("gitui").setup()
require('deferred-clipboard').setup {
  fallback = 'unnamedplus'
}
require("lualine").setup {
	disabled_filetypes = { "lua" }
}
require("neo-tree").setup({
	close_if_last_window = true,
	filesystem = {
		follow_current_file = {
			enabled = true,
			leave_dirs_open = false
		}
	}
});

vim.api.nvim_create_autocmd('CursorMoved', {callback=require('lualine').refresh})

local lsp = require("lspconfig")

vim.g.coq_settings = { auto_start='shut-up' }
local coq = require("coq")

lsp.pyright.setup(coq.lsp_ensure_capabilities({}))
lsp.taplo.setup(coq.lsp_ensure_capabilities({}))
lsp.lua_ls.setup(coq.lsp_ensure_capabilities({}))
lsp.rust_analyzer.setup(coq.lsp_ensure_capabilities({}))

vim.cmd([[:set number]])
vim.cmd([[:set noshowmode]])

vim.g.floaterm_title = "Terminal"
vim.g.floaterm_width = 0.9
vim.g.floaterm_height = 0.9
