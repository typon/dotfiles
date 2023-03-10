local fn = vim.fn
local overrides = require "custom.plugins.overrides"

return {

  -- ["goolord/alpha-nvim"] = { disable = false } -- enables dashboard

  -- Override plugin definition options
  ["neovim/nvim-lspconfig"] = {
    config = function()
      require "plugins.configs.lspconfig"
      require "custom.plugins.lspconfig"
    end,
  },

  -- overrde plugin configs
  ["nvim-treesitter/nvim-treesitter"] = {
    override_options = overrides.treesitter,
  },

  ["williamboman/mason.nvim"] = {
    override_options = overrides.mason,
  },

  ["kyazdani42/nvim-tree.lua"] = {
    override_options = overrides.nvimtree,
  },

  -- Install a plugin
  ["max397574/better-escape.nvim"] = {
    event = "InsertEnter",
    config = function()
      require("better_escape").setup()
    end,
  },

  -- code formatting, linting etc
  ["jose-elias-alvarez/null-ls.nvim"] = {
    after = "nvim-lspconfig",
    config = function()
      require "custom.plugins.null-ls"
    end,
  },

  ["NvChad/ui"] = {
    override_options = {
      statusline = {
        separator_style = "arrow",
        overriden_modules = function()
          return {
            fileInfo = function()
              local sep_style = vim.g.statusline_sep_style
              local separators = require("nvchad_ui.icons").statusline_separators[sep_style]

              local icon = "  "
              local filename = (fn.expand "%" == "" and "Empty ") or fn.expand "%:p"

              if filename ~= "Empty " then
                local devicons_present, devicons = pcall(require, "nvim-web-devicons")

                if devicons_present then
                  local ft_icon = devicons.get_icon(filename)
                  icon = (ft_icon ~= nil and " " .. ft_icon) or ""
                end

                filename = " " .. filename .. " "
              end

              return "%#St_file_info#" .. icon .. filename .. "%#St_file_sep#" .. separators["right"]
            end,
          }
        end,
      },
    }
  },

  ["tpope/vim-fugitive"] = {},
  ["MunifTanjim/nui.nvim"] = {},
  ["dpayne/CodeGPT.nvim"] = {},

  -- remove plugin
  ["lewis6991/gitsigns.nvim"] = false,
}
