package com.zipyrar.videojuegosfirebase.repositories;

import androidx.lifecycle.LiveData;
import androidx.lifecycle.MutableLiveData;

import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.auth.FirebaseUser;
import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.database.ValueEventListener;
import com.zipyrar.videojuegosfirebase.models.Favourite;

import java.util.ArrayList;
import java.util.List;

public class FavouriteRepository {
    private final DatabaseReference favouritesRef;
    private final String currentUserId;

    public FavouriteRepository() {
        FirebaseUser user = FirebaseAuth.getInstance().getCurrentUser();
        currentUserId = (user != null) ? user.getUid() : null;
        favouritesRef = FirebaseDatabase.getInstance()
                .getReference("usuarios")
                .child(currentUserId)
                .child("favoritos");
    }

    public LiveData<List<Favourite>> getUserFavourites() {
        MutableLiveData<List<Favourite>> favouritesLiveData = new MutableLiveData<>();

        if (currentUserId == null) {
            favouritesLiveData.setValue(new ArrayList<>());
            return favouritesLiveData;
        }

        favouritesRef.addValueEventListener(new ValueEventListener() {
            @Override
            public void onDataChange(DataSnapshot snapshot) {
                List<Favourite> favouriteList = new ArrayList<>();
                for (DataSnapshot data : snapshot.getChildren()) {
                    Favourite favourite = data.getValue(Favourite.class);
                    if (favourite != null) {
                        favourite.setId(data.getKey());
                        favouriteList.add(favourite);
                    }
                }
                favouritesLiveData.setValue(favouriteList);
            }

            @Override
            public void onCancelled(DatabaseError error) {
                favouritesLiveData.setValue(null);
            }
        });

        return favouritesLiveData;
    }

    public LiveData<Boolean> addFavourite(String videogameId, Favourite favourite) {
        MutableLiveData<Boolean> successLiveData = new MutableLiveData<>();

        if (currentUserId != null) {
            favouritesRef.child(videogameId)
                    .setValue(favourite)
                    .addOnCompleteListener(task -> successLiveData.setValue(task.isSuccessful()));
        } else {
            successLiveData.setValue(false);
        }

        return successLiveData;
    }

    public LiveData<Boolean> removeFavourite(String videogameId) {
        MutableLiveData<Boolean> successLiveData = new MutableLiveData<>();

        if (currentUserId != null) {
            favouritesRef.child(videogameId)
                    .removeValue()
                    .addOnCompleteListener(task -> successLiveData.setValue(task.isSuccessful()));
        } else {
            successLiveData.setValue(false);
        }

        return successLiveData;
    }
}
