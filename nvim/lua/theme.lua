function apply_colors()
	vim.api.nvim_set_hl(0, "FloatBorder", {bg="black", fg="white"})
	vim.api.nvim_set_hl(0, "NormalFloat", {bg="white"})
	vim.api.nvim_set_hl(0, "TelescopeNormal", {bg="black"})
	vim.api.nvim_set_hl(0, "TelescopeBorder", {bg="white"})
	vim.cmd([[:hi Pmenu ctermbg=black guibg=black]])
	vim.cmd([[:hi Pmenu ctermfg=white guifg=white]])
	vim.cmd([[:hi BufferTabpageFill guibg=red]])
end

vim.api.nvim_create_autocmd('ColorScheme', {
	callback = vim.schedule_wrap(apply_colors),
    
	group = vim.api.nvim_create_augroup('usercolors', {}),
})

apply_colors()
