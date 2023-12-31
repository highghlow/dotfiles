require("mason").setup()
require("barbar").setup()
require("gitui").setup()
vim.api.nvim_create_autocmd(
	'vimEnter',
	{
		command='Neotree'
	}
)

