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

