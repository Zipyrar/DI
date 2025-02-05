package com.zipyrar.videojuegosfirebase.views;

import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.widget.EditText;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;
import androidx.appcompat.app.AppCompatDelegate;
import androidx.lifecycle.ViewModelProvider;

import com.zipyrar.videojuegosfirebase.R;
import com.zipyrar.videojuegosfirebase.viewmodels.LoginViewModel;

public class LoginActivity extends AppCompatActivity {
    private LoginViewModel loginViewModel;
    private SharedPreferences sharedPref;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login);

        loginViewModel = new ViewModelProvider(this).get(LoginViewModel.class);

        loginViewModel.getLoginResult().observe(this, success -> {
            if (success) {
                Toast.makeText(this, "Inicio de sesión exitoso.", Toast.LENGTH_SHORT).show();
                Intent intent = new Intent(LoginActivity.this, DashboardActivity.class);
                startActivity(intent);
                finish();
            }
        });

        loginViewModel.getErrorMessage().observe(this, error -> {
            if (error != null) {
                Toast.makeText(this, error, Toast.LENGTH_SHORT).show();
            }
        });

        findViewById(R.id.botNuevoRegistro).setOnClickListener(v -> registerNewUser());
        findViewById(R.id.botInicio).setOnClickListener(v -> loginUser());

        sharedPref = getSharedPreferences("AppConfig", Context.MODE_PRIVATE);
        boolean darkMode = sharedPref.getBoolean("darkMode", false);
        AppCompatDelegate.setDefaultNightMode(darkMode ?
                AppCompatDelegate.MODE_NIGHT_YES : AppCompatDelegate.MODE_NIGHT_NO);
    }

    private void registerNewUser() {
        Intent intent = new Intent(LoginActivity.this, RegisterActivity.class);
        startActivity(intent);
    }

    private void loginUser() {
        String email = ((EditText) findViewById(R.id.emailInicio)).getText().toString().trim();
        String password = ((EditText) findViewById(R.id.contraInicio)).getText().toString().trim();

        loginViewModel.loginUser(email, password);
    }
}
