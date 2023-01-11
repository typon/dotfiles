local M = {}

M.general = {
  n = {
    [";"] = { ":", "command mode", opts = { nowait = true } },
    ["<C-b>"] = {"<cmd> Telescope buffers<CR>", "Open Telescope buffers"},
  },
}

-- more keybinds!

return M
