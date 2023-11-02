" Plugins will be downloaded under the specified directory.
call plug#begin('~/.local/share/nvim/site/plugged')

" Color theme plugins
Plug 'morhetz/gruvbox'

" Use release branch (recommended)
Plug 'neoclide/coc.nvim', {'branch': 'release'}
let g:coc_global_extensions = [ 'coc-clangd', 'coc-css', 'coc-html', 'coc-java', 'coc-json', 'coc-markdownlint', 'coc-phpls', 'coc-rust-analyzer', 'coc-sh', 'coc-sumneko-lua', 'coc-yank', 'coc-prettier', 'coc-emmet', 'coc-tsserver', 'coc-tslint-plugin', '@yaegassy/coc-volar', '@yaegassy/coc-typescript-vue-plugin', '@yaegassy/coc-tailwindcss3']

"------------------------ VIM TSX ------------------------
" by default, if you open tsx file, neovim does not show syntax colors
" vim-tsx will do all the coloring for jsx in the .tsx file
Plug 'ianks/vim-tsx'
Plug 'leafgarland/typescript-vim'
Plug 'peitalin/vim-jsx-typescript'
Plug 'airblade/vim-gitgutter'

" List ends here. Plugins become visible to Vim after this call.
call plug#end()

" == AUTOCMD ================================ 
" by default .ts file are not identified as typescript and .tsx files are not
" identified as typescript react file, so add following
au BufNewFile,BufRead *.ts setlocal filetype=typescript
au BufNewFile,BufRead *.tsx setlocal filetype=typescript.tsx
" == AUTOCMD END ================================

"""""""""""""""""""""""""""""""""""""""""""""""""
" Color Settings
"""""""""""""""""""""""""""""""""""""""""""""""""
syntax on
colorscheme gruvbox

"""""""""""""""""""""""""""""""""""""""""""""""""
" UI Settings
"""""""""""""""""""""""""""""""""""""""""""""""""
" Keep cursor in the middle of the page, useful for editing text
set so=999

"""""""""""""""""""""""""""""""""""""""""""""""""
" EDITOR Settings
"""""""""""""""""""""""""""""""""""""""""""""""""

" Setup Coc Stuff
set tabstop=4
set shiftwidth=4
set expandtab
set nu! rnu!
set clipboard=unnamedplus

" Use tab for trigger completion with characters ahead and navigate
" NOTE: There's always complete item selected by default, you may want to enable
" no select by `"suggest.noselect": true` in your configuration file
" NOTE: Use command ':verbose imap <tab>' to make sure tab is not mapped by
" other plugin before putting this into your config
inoremap <silent><expr> <TAB>
      \ coc#pum#visible() ? coc#pum#next(1) :
      \ CheckBackspace() ? "\<Tab>" :
      \ coc#refresh()
inoremap <expr><S-TAB> coc#pum#visible() ? coc#pum#prev(1) : "\<C-h>"

function! CheckBackspace() abort
  let col = col('.') - 1
  return !col || getline('.')[col - 1]  =~# '\s'
endfunction

" Some servers have issues with backup files, see #649
set nobackup
set nowritebackup

" Having longer updatetime (default is 4000 ms = 4s) leads to noticeable
" delays and poor user experience
set updatetime=300

" Always show the signcolumn, otherwise it would shift the text each time
" diagnostics appear/become resolved
set signcolumn=yes

" Use <c-space> to trigger completion
if has('nvim')
  inoremap <silent><expr> <c-space> coc#refresh()
else
  inoremap <silent><expr> <c-@> coc#refresh()
endif

" GoTo code navigation
nmap <silent> gd <Plug>(coc-definition)
nmap <silent> gy <Plug>(coc-type-definition)
nmap <silent> gi <Plug>(coc-implementation)
nmap <silent> gr <Plug>(coc-references)

" Use K to show documentation in preview window
nnoremap <silent> K :call ShowDocumentation()<CR>

function! ShowDocumentation()
  if CocAction('hasProvider', 'hover')
    call CocActionAsync('doHover')
  else
    call feedkeys('K', 'in')
  endif
endfunction
