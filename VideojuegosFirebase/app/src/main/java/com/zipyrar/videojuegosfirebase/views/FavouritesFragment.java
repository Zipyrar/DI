package com.zipyrar.videojuegosfirebase.views;

import android.os.Bundle;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.fragment.app.Fragment;
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

public class FavouritesFragment extends Fragment {
    private RecyclerView favouritesRecyclerView;
    private FavouritesAdapter favouritesAdapter;
    private List<Favourite> favouritesList;
    private DatabaseReference databaseRef;
    private String userId;

    @Nullable
    @Override
    public View onCreateView(@NonNull LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {
        View view = inflater.inflate(R.layout.fragment_favourites, container, false);

        favouritesRecyclerView = view.findViewById(R.id.recyclerViewFavourites);
        favouritesRecyclerView.setLayoutManager(new LinearLayoutManager(requireContext())); // Usar requireContext()

        favouritesList = new ArrayList<>();
        favouritesAdapter = new FavouritesAdapter(requireContext(), favouritesList); // Usar requireContext()

        favouritesRecyclerView.setAdapter(favouritesAdapter);

        FirebaseUser currentUser = FirebaseAuth.getInstance().getCurrentUser();
        if (currentUser != null) {
            userId = currentUser.getUid();
        } else {
            Log.e("FavouritesFragment", "Usuario no autenticado");
            return view;
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

        return view;
    }
}