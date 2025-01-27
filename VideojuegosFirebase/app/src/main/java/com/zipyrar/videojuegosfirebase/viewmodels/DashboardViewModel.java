package com.zipyrar.videojuegosfirebase.viewmodels;

import androidx.annotation.NonNull;
import androidx.lifecycle.LiveData;
import androidx.lifecycle.MutableLiveData;
import androidx.lifecycle.ViewModel;

import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.database.ValueEventListener;
import com.zipyrar.videojuegosfirebase.models.Videogame;

import java.util.ArrayList;
import java.util.List;

public class DashboardViewModel extends ViewModel {
    private final MutableLiveData<List<Videogame>> videogames = new MutableLiveData<>();
    private final DatabaseReference databaseRef;

    public DashboardViewModel() {
        databaseRef = FirebaseDatabase.getInstance().getReference("videojuegos");

        databaseRef.addValueEventListener(new ValueEventListener() {
            @Override
            public void onDataChange(@NonNull DataSnapshot snapshot) {
                List<Videogame> videogameList = new ArrayList<>();
                for (DataSnapshot data : snapshot.getChildren()) {
                    Videogame videogame = data.getValue(Videogame.class);
                    if (videogame != null) {
                        videogameList.add(videogame);
                    }
                }
                videogames.setValue(videogameList);
            }

            @Override
            public void onCancelled(@NonNull DatabaseError error) {
                videogames.setValue(null);
            }
        });
    }

    public LiveData<List<Videogame>> getVideogames() {
        return videogames;
    }
}
