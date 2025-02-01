package com.zipyrar.videojuegosfirebase.views;

import android.content.Intent;
import android.os.Bundle;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

import com.bumptech.glide.Glide;
import com.google.android.material.floatingactionbutton.FloatingActionButton;
import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.zipyrar.videojuegosfirebase.R;
import com.zipyrar.videojuegosfirebase.models.Favourite;
import com.zipyrar.videojuegosfirebase.models.Videogame;
import com.zipyrar.videojuegosfirebase.repositories.UserRepository;

public class DetailActivity extends AppCompatActivity {
    private DatabaseReference userFavoritesRef;
    private UserRepository userRepository;
    private boolean isFavourite = false;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_detail);

        TextView titleView = findViewById(R.id.detailTitle);
        ImageView imageView = findViewById(R.id.detailImage);
        TextView descriptionView = findViewById(R.id.detailDescription);
        FloatingActionButton btnFavorite = findViewById(R.id.btnFavorite);

        String title = getIntent().getStringExtra("titulo");
        String imageUrl = getIntent().getStringExtra("imagen");
        String description = getIntent().getStringExtra("descripcion");
        String videogameNumber = getIntent().getStringExtra("id");

        if (title != null) titleView.setText(title);
        if (description != null) descriptionView.setText(description);
        if (imageUrl != null) Glide.with(this).load(imageUrl).into(imageView);

        userRepository = new UserRepository();

        String userId = userRepository.getCurrentUserId();

        if (userId != null) {
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
                        Toast.makeText(DetailActivity.this, "Error al verificar los favoritos", Toast.LENGTH_SHORT).show();
                    });
        } else {
            Toast.makeText(DetailActivity.this, "No hay usuario autenticado", Toast.LENGTH_SHORT).show();
        }

        btnFavorite.setOnClickListener(view -> {
            if (isFavourite) {
                userRepository.removeFavorite(videogameNumber).observe(this, success -> {
                    if (success) {
                        isFavourite = false;
                        btnFavorite.setImageResource(R.drawable.star_no_favorite);
                        Toast.makeText(DetailActivity.this, "Eliminado de favoritos", Toast.LENGTH_SHORT).show();
                    } else {
                        Toast.makeText(DetailActivity.this, "Error al eliminar de favoritos", Toast.LENGTH_SHORT).show();
                    }
                });
            } else {
                Favourite favourite = new Favourite(title, description, imageUrl);
                userRepository.addFavorite(videogameNumber, favourite).observe(this, success -> {
                    if (success) {
                        isFavourite = true;
                        btnFavorite.setImageResource(R.drawable.star_favorite);
                        Toast.makeText(DetailActivity.this, "Añadido a favoritos", Toast.LENGTH_SHORT).show();
                    } else {
                        Toast.makeText(DetailActivity.this, "Error al añadir a favoritos", Toast.LENGTH_SHORT).show();
                    }
                });
            }
        });
    }
}

