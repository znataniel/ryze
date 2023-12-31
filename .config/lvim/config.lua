-- Read the docs: https://www.lunarvim.org/docs/configuration
-- Video Tutorials: https://www.youtube.com/watch?v=sFA9kX-Ud_c&list=PLhoH5vyxr6QqGu0i7tt_XoVK9v-KvZ3m6
-- Forum: https://www.reddit.com/r/lunarvim/
-- Discord: https://discord.com/invite/Xb9B4Ny
lvim.format_on_save.enabled = true
require("lvim.lsp.manager").setup("emmet_ls")
require("lvim.lsp.manager").setup("css_lsp")


local formatters = require "lvim.lsp.null-ls.formatters"
formatters.setup {
  { name = "yapf" },
  { name = "latexindent" },
  { name = "prettier" },
}
