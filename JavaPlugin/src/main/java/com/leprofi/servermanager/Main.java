package com.leprofi.servermanager;

import org.bukkit.Bukkit;
import org.bukkit.plugin.java.JavaPlugin;

public final class Main extends JavaPlugin {

    @Override
    public void onEnable() {
        // Plugin startup logic

    }

    @Override
    public void onDisable() {
        // Plugin shutdown logic
    }

    public void ToggleWhitelist() {
        if(Bukkit.getServer().hasWhitelist()) {
            Bukkit.setWhitelist(false);
        } else {
            Bukkit.setWhitelist(true);
        }
    }
}
