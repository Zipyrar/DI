package com.zipyrar.videojuegosfirebase.repositories;

import androidx.lifecycle.LiveData;
import androidx.lifecycle.MutableLiveData;

import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.auth.FirebaseUser;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.zipyrar.videojuegosfirebase.models.User;

public class UserRepository {
    private FirebaseAuth mAuth;
    private DatabaseReference databaseRef;

    public UserRepository() {
        mAuth = FirebaseAuth.getInstance();
        databaseRef = FirebaseDatabase.getInstance().getReference("usuarios");
    }

    public LiveData<Boolean> registerUser(String email, String password, User user) {
        MutableLiveData<Boolean> result = new MutableLiveData<>();
        mAuth.createUserWithEmailAndPassword(email, password)
                .addOnCompleteListener(task -> {
                    if (task.isSuccessful()) {
                        FirebaseUser firebaseUser = mAuth.getCurrentUser();
                        if (firebaseUser != null) {
                            databaseRef.child(firebaseUser.getUid()).setValue(user)
                                    .addOnSuccessListener(aVoid -> result.setValue(true))
                                    .addOnFailureListener(e -> result.setValue(false));
                        }
                    } else {
                        result.setValue(false);
                    }
                });
        return result;
    }

    public LiveData<Boolean> loginUser(String email, String password) {
        MutableLiveData<Boolean> loginResult = new MutableLiveData<>();
        mAuth.signInWithEmailAndPassword(email, password)
                .addOnCompleteListener(task -> {
                    if (task.isSuccessful()) {
                        loginResult.setValue(true);
                    } else {
                        loginResult.setValue(false);
                    }
                });
        return loginResult;
    }
}
