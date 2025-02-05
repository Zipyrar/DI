package com.zipyrar.videojuegosfirebase.views;

import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.Toast;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;
import androidx.appcompat.app.AppCompatDelegate;
import androidx.lifecycle.ViewModelProvider;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import com.google.firebase.auth.FirebaseAuth;
import com.zipyrar.videojuegosfirebase.R;
import com.zipyrar.videojuegosfirebase.adapters.VideogameAdapter;
import com.zipyrar.videojuegosfirebase.viewmodels.DashboardViewModel;

import java.util.List;

public class DashboardActivity extends AppCompatActivity {
    private FirebaseAuth mAuth;
    private DashboardViewModel viewModel;
    private VideogameAdapter adapter;
    private SharedPreferences sharedPref;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_dashboard);

        mAuth = FirebaseAuth.getInstance();
        viewModel = new ViewModelProvider(this).get(DashboardViewModel.class);

        RecyclerView recyclerView = findViewById(R.id.recyclerView);
        Button logoutButton = findViewById(R.id.btnCierre);
        Button favouritesButton = findViewById(R.id.btnFavourites);
        Button ThemeButton = findViewById(R.id.btnThemeMode);

        adapter = new VideogameAdapter(this, List.of());
        recyclerView.setAdapter(adapter);
        recyclerView.setLayoutManager(new LinearLayoutManager(this));

        viewModel.getVideogames().observe(this, videogames -> {
            if (videogames != null) {
                adapter = new VideogameAdapter(this, videogames);
                recyclerView.setAdapter(adapter);
            } else {
                Toast.makeText(this, "Error al cargar datos.", Toast.LENGTH_SHORT).show();
            }
        });

        logoutButton.setOnClickListener(v -> {
            mAuth.signOut();
            Toast.makeText(this, "Cerraste sesión", Toast.LENGTH_SHORT).show();
            Intent intent = new Intent(DashboardActivity.this, LoginActivity.class);
            startActivity(intent);
            finish();
        });

        favouritesButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(DashboardActivity.this, FavouritesActivity.class);
                startActivity(intent);
            }
        });

        sharedPref = getSharedPreferences("AppConfig", Context.MODE_PRIVATE);
        boolean darkMode = sharedPref.getBoolean("darkMode", false);
        AppCompatDelegate.setDefaultNightMode(darkMode ?
                AppCompatDelegate.MODE_NIGHT_YES : AppCompatDelegate.MODE_NIGHT_NO);

        ThemeButton.setOnClickListener(view -> {
            boolean isDarkMode = sharedPref.getBoolean("darkMode", false);
            sharedPref.edit().putBoolean("darkMode", !isDarkMode).apply();

            AppCompatDelegate.setDefaultNightMode(isDarkMode ?
                    AppCompatDelegate.MODE_NIGHT_NO : AppCompatDelegate.MODE_NIGHT_YES);
        });
    }
}

