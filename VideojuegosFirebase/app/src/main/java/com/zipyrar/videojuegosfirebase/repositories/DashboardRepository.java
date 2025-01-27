package com.zipyrar.videojuegosfirebase.repositories;

import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.database.ValueEventListener;
import com.zipyrar.videojuegosfirebase.models.Videogame;

import java.util.ArrayList;
import java.util.List;

import androidx.annotation.NonNull;
import androidx.lifecycle.LiveData;
import androidx.lifecycle.MutableLiveData;

public class DashboardRepository {
    private DatabaseReference databaseRef;

    public DashboardRepository() {
        databaseRef = FirebaseDatabase.getInstance().getReference("videojuegos");
    }

    public LiveData<List<Videogame>> getVideogames() {
        MutableLiveData<List<Videogame>> data = new MutableLiveData<>();
        databaseRef.addValueEventListener(new ValueEventListener() {
            @Override
            public void onDataChange(@NonNull DataSnapshot snapshot) {
                List<Videogame> videogames = new ArrayList<>();
                for (DataSnapshot child : snapshot.getChildren()) {
                    Videogame videogame = child.getValue(Videogame.class);
                    videogames.add(videogame);
                }
                data.setValue(videogames);
            }

            @Override
            public void onCancelled(@NonNull DatabaseError error) {
                data.setValue(null);
            }
        });
        return data;
    }
}

