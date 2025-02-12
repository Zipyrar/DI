package com.zipyrar.videojuegosfirebase.views;

import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.fragment.app.Fragment;

import com.bumptech.glide.Glide;
import com.google.android.material.floatingactionbutton.FloatingActionButton;
import com.zipyrar.videojuegosfirebase.R;
import com.zipyrar.videojuegosfirebase.models.Favourite;
import com.zipyrar.videojuegosfirebase.repositories.UserRepository;

public class DetailFragment extends Fragment {
    private UserRepository userRepository;
    private boolean isFavourite = false;
    private String videogameNumber;

    public DetailFragment() {
        // Constructor vacío requerido para los fragmentos
    }

    public static DetailFragment newInstance(String title, String imageUrl, String description, String id) {
        DetailFragment fragment = new DetailFragment();
        Bundle args = new Bundle();
        args.putString("titulo", title);
        args.putString("imagen", imageUrl);
        args.putString("descripcion", description);
        args.putString("id", id);
        fragment.setArguments(args);
        return fragment;
    }

    @Nullable
    @Override
    public View onCreateView(@NonNull LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {
        return inflater.inflate(R.layout.fragment_detail, container, false);
    }

    @Override
    public void onViewCreated(@NonNull View view, @Nullable Bundle savedInstanceState) {
        super.onViewCreated(view, savedInstanceState);

        TextView titleView = view.findViewById(R.id.detailTitle);
        ImageView imageView = view.findViewById(R.id.detailImage);
        TextView descriptionView = view.findViewById(R.id.detailDescription);
        FloatingActionButton btnFavorite = view.findViewById(R.id.btnFavorite);

        Bundle args = getArguments();
        if (args != null) {
            String title = args.getString("titulo");
            String imageUrl = args.getString("imagen");
            String description = args.getString("descripcion");
            videogameNumber = args.getString("id");

            if (title != null) titleView.setText(title);
            if (description != null) descriptionView.setText(description);
            if (imageUrl != null) Glide.with(requireContext()).load(imageUrl).into(imageView);
        }

        userRepository = new UserRepository();
        String userId = userRepository.getCurrentUserId();

        if (userId != null && videogameNumber != null) {
            userRepository.databaseRef.child(userId)
                    .child("favoritos")
                    .child(videogameNumber)
                    .get()
                    .addOnSuccessListener(snapshot -> {
                        if (snapshot.exists()) {
                            isFavourite = true;
                            btnFavorite.setImageResource(R.drawable.star_favorite);
                        } else {
                            isFavourite = false;
                            btnFavorite.setImageResource(R.drawable.star_no_favorite);
                        }
                    })
                    .addOnFailureListener(e -> {
                        Toast.makeText(requireContext(), "Error al verificar los favoritos", Toast.LENGTH_SHORT).show();
                    });
        } else {
            Toast.makeText(requireContext(), "No hay usuario autenticado", Toast.LENGTH_SHORT).show();
        }

        btnFavorite.setOnClickListener(v -> {
            if (isFavourite) {
                userRepository.removeFavorite(videogameNumber).observe(getViewLifecycleOwner(), success -> {
                    if (success) {
                        isFavourite = false;
                        btnFavorite.setImageResource(R.drawable.star_no_favorite);
                        Toast.makeText(requireContext(), "Eliminado de favoritos", Toast.LENGTH_SHORT).show();
                    } else {
                        Toast.makeText(requireContext(), "Error al eliminar de favoritos", Toast.LENGTH_SHORT).show();
                    }
                });
            } else {
                Favourite favourite = new Favourite(args.getString("titulo"), args.getString("descripcion"), args.getString("imagen"));
                userRepository.addFavorite(videogameNumber, favourite).observe(getViewLifecycleOwner(), success -> {
                    if (success) {
                        isFavourite = true;
                        btnFavorite.setImageResource(R.drawable.star_favorite);
                        Toast.makeText(requireContext(), "Añadido a favoritos", Toast.LENGTH_SHORT).show();
                    } else {
                        Toast.makeText(requireContext(), "Error al añadir a favoritos", Toast.LENGTH_SHORT).show();
                    }
                });
            }
        });
    }
}