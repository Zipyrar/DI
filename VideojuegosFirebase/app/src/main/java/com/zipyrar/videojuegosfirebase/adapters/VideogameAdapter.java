package com.zipyrar.videojuegosfirebase.adapters;
import android.content.Context;
import android.content.Intent;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import com.bumptech.glide.Glide;
import com.zipyrar.videojuegosfirebase.R;
import com.zipyrar.videojuegosfirebase.models.Videogame;

import java.util.List;

public class VideogameAdapter extends RecyclerView.Adapter<VideogameAdapter.ViewHolder> {
    private List<Videogame> videogames;
    private Context context;

    public VideogameAdapter(Context context, List<Videogame> videogames) {
        this.context = context;
        this.videogames = videogames;
    }

    @NonNull
    @Override
    public ViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        View view = LayoutInflater.from(context).inflate(R.layout.item_videogame, parent, false);
        return new ViewHolder(view);
    }

    @Override
    public void onBindViewHolder(@NonNull ViewHolder holder, int position) {
        Videogame videogame = videogames.get(position);

        holder.titleView.setText(videogame.getTitulo());
        holder.descriptionView.setText(videogame.getDescripcion());
        Glide.with(context).load(videogame.getImagen()).into(holder.imageView);

        holder.itemView.setOnClickListener(v -> {
            Intent intent = new Intent(context, DetailActivity.class);
            intent.putExtra("titulo", videogame.getTitulo());
            intent.putExtra("imagen", videogame.getImagen());
            intent.putExtra("descripcion", videogame.getDescripcion());
            intent.putExtra("id", videogame.getId());
            context.startActivity(intent);
        });
    }

    @Override
    public int getItemCount() {
        return videogames.size();
    }

    static class ViewHolder extends RecyclerView.ViewHolder {
        TextView titleView;
        TextView descriptionView;
        ImageView imageView;

        public ViewHolder(@NonNull View itemView) {
            super(itemView);
            titleView = itemView.findViewById(R.id.tituloItem);
            descriptionView = itemView.findViewById(R.id.descripcionItem);
            imageView = itemView.findViewById(R.id.imagenItem);
        }
    }
}
