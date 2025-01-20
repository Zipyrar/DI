package com.zipyrar.videojuegosfirebase;
import android.os.Bundle;
import android.util.Log;
import android.widget.EditText;
import android.widget.Toast;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

import com.google.firebase.Firebase;
import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.auth.FirebaseUser;
import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.database.ValueEventListener;

import java.util.Calendar;

public class RegisterActivity extends AppCompatActivity {
    private FirebaseAuth mAuth;
    private DatabaseReference databaseRef;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_register);

        mAuth = FirebaseAuth.getInstance();
        databaseRef = FirebaseDatabase.getInstance().getReference();


        findViewById(R.id.botRegistro).setOnClickListener(v -> registerUser());
    }

    private void registerUser() {
        String email = ((EditText) findViewById(R.id.emailRegistro)).getText().toString();
        String password = ((EditText) findViewById(R.id.contraRegistro)).getText().toString();
        String confirmP = ((EditText) findViewById(R.id.contraConfirRegistro)).getText().toString();
        String name = ((EditText) findViewById(R.id.nombreRegistro)).getText().toString().trim();
        String phone = ((EditText) findViewById(R.id.telefonoRegistro)).getText().toString().trim();
        String direction = ((EditText) findViewById(R.id.direccionRegistro)).getText().toString().trim();

        if (email.isEmpty() || password.isEmpty() || confirmP.isEmpty() || name.isEmpty() || phone.isEmpty() || direction.isEmpty()) {
            Toast.makeText(this, "Por favor, completa todos los campos.", Toast.LENGTH_SHORT).show();
            return;
        }
        if (!password.equals(confirmP)) {
            Toast.makeText(this, "Las contraseñas no coinciden.", Toast.LENGTH_SHORT).show();
            return;
        }

        mAuth.createUserWithEmailAndPassword(email, password)
                .addOnCompleteListener(this, task -> {
                    if (task.isSuccessful()) {
                        FirebaseUser firebaseUser = mAuth.getCurrentUser();
                        if (firebaseUser != null) {
                            firebaseUser.reload().addOnCompleteListener(reloadTask -> {
                                String uid = firebaseUser.getUid();
                                User newUser = new User(name, phone, direction);

                                databaseRef.child(uid).setValue(newUser)
                                        .addOnSuccessListener(aVoid -> {
                                            Toast.makeText(RegisterActivity.this, "Usuario registrado exitosamente.", Toast.LENGTH_SHORT).show();
                                        })
                                        .addOnFailureListener(e -> {
                                            Toast.makeText(RegisterActivity.this, "Error en el registro: " + task.getException().getMessage(), Toast.LENGTH_SHORT).show();
                                            Log.e("Firebase", "Error al guardar en la base de datos.", e);
                                        });
                            });
                        }
                        Toast.makeText(RegisterActivity.this, "Usuario registrado correctamente.", Toast.LENGTH_SHORT).show();
                    }
                });
    }

    public static class User {
        public String name;
        public String phone;
        public String direction;

        public User() {}

        public User(String name, String phone, String direction) {
            this.name = name;
            this.phone = phone;
            this.direction = direction;
        }
    }
}