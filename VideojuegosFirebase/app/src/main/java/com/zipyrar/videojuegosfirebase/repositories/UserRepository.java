package com.zipyrar.videojuegosfirebase.repositories;

import androidx.lifecycle.LiveData;
import androidx.lifecycle.MutableLiveData;

import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.auth.FirebaseUser;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.zipyrar.videojuegosfirebase.models.Favourite;
import com.zipyrar.videojuegosfirebase.models.User;

public class UserRepository {
    private FirebaseAuth mAuth;
    public DatabaseReference databaseRef;
    private String currentUserId;

    public UserRepository() {
        mAuth = FirebaseAuth.getInstance();
        databaseRef = FirebaseDatabase.getInstance().getReference("usuarios");
        currentUserId = FirebaseAuth.getInstance().getCurrentUser().getUid();
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

    public String getCurrentUserId() {
        return currentUserId;
    }

    public LiveData<Boolean> addFavorite(String videogameNumber, Favourite favourite) {

        MutableLiveData<Boolean> successLiveData = new MutableLiveData<>();

        if (currentUserId != null) {
            databaseRef.child(currentUserId)
                    .child("favoritos")
                    .child(videogameNumber)
                    .setValue(favourite)
                    .addOnCompleteListener(task -> {
                        if (task.isSuccessful()) {
                            successLiveData.setValue(true);
                        } else {
                            successLiveData.setValue(false);
                        }
                    });
        } else {
            successLiveData.setValue(false);
        }

        return successLiveData;
    }

    public LiveData<Boolean> removeFavorite(String videogameNumber) {
        MutableLiveData<Boolean> successLiveData = new MutableLiveData<>();

        if (currentUserId != null) {
            databaseRef.child(currentUserId)
                    .child("favoritos")
                    .child(videogameNumber)
                    .removeValue()
                    .addOnCompleteListener(task -> {
                        if (task.isSuccessful()) {
                            successLiveData.setValue(true);
                        } else {
                            successLiveData.setValue(false);
                        }
                    });
        } else {
            successLiveData.setValue(false);
        }

        return successLiveData;
    }
}
