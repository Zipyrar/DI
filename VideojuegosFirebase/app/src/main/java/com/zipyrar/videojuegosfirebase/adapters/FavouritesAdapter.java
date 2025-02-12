package com.zipyrar.videojuegosfirebase.adapters;

import android.content.Context;
import android.content.Intent;
import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import com.bumptech.glide.Glide;
import com.zipyrar.videojuegosfirebase.R;
import com.zipyrar.videojuegosfirebase.models.Favourite;
import com.zipyrar.videojuegosfirebase.views.DetailFragment;

import java.util.List;

public class FavouritesAdapter extends RecyclerView.Adapter<FavouritesAdapter.ViewHolder> {
    private List<Favourite> favourites;
    private Context context;

    // Cambié el constructor para aceptar el contexto
    public FavouritesAdapter(Context context, List<Favourite> favourites) {
        this.context = context;
        this.favourites = favourites;
    }

    @NonNull
    @Override
    public FavouritesAdapter.ViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        // Usa el contexto para inflar la vista
        View view = LayoutInflater.from(context).inflate(R.layout.item_videogame, parent, false);
        return new ViewHolder(view);
    }

    @Override
    public void onBindViewHolder(@NonNull FavouritesAdapter.ViewHolder holder, int position) {
        Favourite favourite = favourites.get(position);

        holder.titleView.setText(favourite.getTitulo());
        holder.descriptionView.setText(favourite.getDescripcion());
        Glide.with(context).load(favourite.getImagen()).into(holder.imageView);

        holder.itemView.setOnClickListener(v -> {
            DetailFragment detailFragment = new DetailFragment();

            Bundle bundle = new Bundle();
            bundle.putString("titulo", favourite.getTitulo());
            bundle.putString("imagen", favourite.getImagen());
            bundle.putString("descripcion", favourite.getDescripcion());
            bundle.putString("id", favourite.getId());

            detailFragment.setArguments(bundle);


            if (context instanceof androidx.fragment.app.FragmentActivity) {
                androidx.fragment.app.FragmentActivity activity = (androidx.fragment.app.FragmentActivity) context;

                activity.getSupportFragmentManager()
                        .beginTransaction()
                        .replace(R.id.fragmentContainer, detailFragment)
                        .addToBackStack(null)
                        .commit();
            }
        });
    }

    @Override
    public int getItemCount() {
        return favourites.size();
    }

    public void updateData(List<Favourite> newFavourites) {
        this.favourites.clear();
        this.favourites.addAll(newFavourites);
        notifyDataSetChanged();
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
