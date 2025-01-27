package com.zipyrar.videojuegosfirebase.views;

import android.os.Bundle;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

import com.bumptech.glide.Glide;
import com.zipyrar.videojuegosfirebase.R;
import com.zipyrar.videojuegosfirebase.models.Videogame;

public class DetailActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_detail);

        TextView titleView = findViewById(R.id.detailTitle);
        ImageView imageView = findViewById(R.id.detailImage);
        TextView descriptionView = findViewById(R.id.detailDescription);

        String title = getIntent().getStringExtra("titulo");
        String imageUrl = getIntent().getStringExtra("imagen");
        String description = getIntent().getStringExtra("descripcion");

        if (title != null) titleView.setText(title);
        if (description != null) descriptionView.setText(description);
        if (imageUrl != null) Glide.with(this).load(imageUrl).into(imageView);
    }
}

