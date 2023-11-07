package com.example.mycatalog;

import androidx.activity.OnBackPressedCallback;
import androidx.annotation.NonNull;
import androidx.appcompat.app.ActionBarDrawerToggle;
import androidx.appcompat.app.AppCompatActivity;
import androidx.appcompat.widget.Toolbar;
import androidx.core.view.GravityCompat;
import androidx.drawerlayout.widget.DrawerLayout;
import androidx.fragment.app.Fragment;

import android.content.Context;
import android.content.Intent;
import android.os.Bundle;
import android.view.MenuItem;
import android.view.View;
import android.widget.Button;

import com.google.android.material.navigation.NavigationView;

public class MainActivity extends AppCompatActivity  {
    private Context context = this;
    private DrawerLayout drawerLayout;
    private Toolbar toolbar;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        //inicializamos los atributos
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        drawerLayout = findViewById(R.id.drawer_layout);
        toolbar = findViewById(R.id.toolbar);

        //creamos metodo que cierre el menu y no la app
        getOnBackPressedDispatcher().addCallback(this, new OnBackPressedCallback(true) {
            //metodo que cierra el menu si se pulsa atrás.
            @Override
            public void handleOnBackPressed() {
                if (drawerLayout.isDrawerOpen(GravityCompat.START)){
                    drawerLayout.closeDrawer(GravityCompat.START);
                }else{
                    if (isEnabled()){
                        setEnabled(false);
                        MainActivity.super.onBackPressed();
                    }
                }
            }
        });

        setSupportActionBar(toolbar);
        ActionBarDrawerToggle toggle = new ActionBarDrawerToggle(
                this, drawerLayout, toolbar, R.string.navigation_drawer_open, R.string.navigation_drawer_close);
        drawerLayout.addDrawerListener(toggle);
        toggle.syncState();

        NavigationView navigationView = findViewById(R.id.navigation_view);
        //creamos el elemento que escuchara en cual boton clickamos de nuestro menú
        navigationView.setNavigationItemSelectedListener(new NavigationView.OnNavigationItemSelectedListener() {
            @Override
            public boolean onNavigationItemSelected(@NonNull MenuItem item) {
                // menu que lleva a sus actividades
                Fragment fragment = null;
                if (item.getItemId() == R.id.nav_catalog) {
                    // Navega a al fragment1 .. Carlos ponme un 70
                    fragment = new Fragment1();

                }else if(item.getItemId() == R.id.nav_about){
                    fragment = new Fragment3();
                }
                //si no llega ningun fragment
                if (fragment != null){
                    getSupportFragmentManager().beginTransaction().replace(R.id.fragment_container, fragment).commit();
                    drawerLayout.closeDrawer(GravityCompat.START);
                    return true;
                }
                // Cierra el Navigation Drawer después de la selección
                return false;

            }
        });
    }
}