package com.zipyrar.videojuegosfirebase.views;

import android.os.Bundle;
import android.widget.EditText;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;
import androidx.lifecycle.ViewModelProvider;

import com.zipyrar.videojuegosfirebase.R;
import com.zipyrar.videojuegosfirebase.viewmodels.RegisterViewModel;

public class RegisterActivity extends AppCompatActivity {
    private RegisterViewModel registerViewModel;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_register);

        registerViewModel = new ViewModelProvider(this).get(RegisterViewModel.class);

        registerViewModel.getRegistrationResult().observe(this, success -> {
            if (success) {
                Toast.makeText(this, "Usuario registrado exitosamente.", Toast.LENGTH_SHORT).show();
                finish(); //Cierra esta actividad después del registro exitoso.
            }
        });

        registerViewModel.getErrorMessage().observe(this, error -> {
            if (error != null) {
                Toast.makeText(this, error, Toast.LENGTH_SHORT).show();
            }
        });

        findViewById(R.id.botRegistro).setOnClickListener(v -> {
            String email = ((EditText) findViewById(R.id.emailRegistro)).getText().toString().trim();
            String password = ((EditText) findViewById(R.id.contraRegistro)).getText().toString().trim();
            String confirmP = ((EditText) findViewById(R.id.contraConfirRegistro)).getText().toString().trim();
            String name = ((EditText) findViewById(R.id.nombreRegistro)).getText().toString().trim();
            String phone = ((EditText) findViewById(R.id.telefonoRegistro)).getText().toString().trim();
            String direction = ((EditText) findViewById(R.id.direccionRegistro)).getText().toString().trim();

            registerViewModel.registerUser(email, password, confirmP, name, phone, direction);
        });
    }
}
