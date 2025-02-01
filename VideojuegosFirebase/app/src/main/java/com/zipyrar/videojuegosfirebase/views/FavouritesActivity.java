package com.zipyrar.videojuegosfirebase.views;

import android.os.Bundle;
import android.util.Log;
import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;
import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.auth.FirebaseUser;
import com.google.firebase.database.*;
import com.zipyrar.videojuegosfirebase.R;
import com.zipyrar.videojuegosfirebase.adapters.FavouritesAdapter;
import com.zipyrar.videojuegosfirebase.models.Favourite;
import java.util.ArrayList;
import java.util.List;

public class FavouritesActivity extends AppCompatActivity {
    private RecyclerView favouritesRecyclerView;
    private FavouritesAdapter favouritesAdapter;
    private List<Favourite> favouritesList;
    private DatabaseReference databaseRef;
    private String userId;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_favourites);

        favouritesRecyclerView = findViewById(R.id.recyclerViewFavourites);
        favouritesRecyclerView.setLayoutManager(new LinearLayoutManager(this));

        favouritesList = new ArrayList<>();
        favouritesAdapter = new FavouritesAdapter(this, favouritesList);

        favouritesRecyclerView.setAdapter(favouritesAdapter);

        FirebaseUser currentUser = FirebaseAuth.getInstance().getCurrentUser();
        if (currentUser != null) {
            userId = currentUser.getUid();
        } else {
            Log.e("FavouritesActivity", "Usuario no autenticado");
            return;
        }

        databaseRef = FirebaseDatabase.getInstance().getReference("usuarios");

        databaseRef.child(userId).child("favoritos").addValueEventListener(new ValueEventListener() {
            @Override
            public void onDataChange(@NonNull DataSnapshot dataSnapshot) {
                favouritesList.clear();
                for (DataSnapshot snapshot : dataSnapshot.getChildren()) {
                    String id = snapshot.getKey();
                    Favourite favourite = snapshot.getValue(Favourite.class);
                    if (favourite != null) {
                        favourite.setId(id);
                        favouritesList.add(favourite);
                        Log.d("Firebase", "Favorito encontrado: " + favourite.getTitulo());
                    }
                }

                if (favouritesList.isEmpty()) {
                    Log.d("Firebase", "No se encontraron favoritos");
                }

                favouritesAdapter.notifyDataSetChanged();
            }

            @Override
            public void onCancelled(@NonNull DatabaseError databaseError) {
                Log.e("Firebase", "Error al recuperar datos de favoritos: " + databaseError.getMessage());
            }
        });
    }
}