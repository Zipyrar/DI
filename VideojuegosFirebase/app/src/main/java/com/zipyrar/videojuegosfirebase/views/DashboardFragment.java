package com.zipyrar.videojuegosfirebase.views;

import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.Toast;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatDelegate;
import androidx.fragment.app.Fragment;
import androidx.lifecycle.ViewModelProvider;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import com.google.firebase.auth.FirebaseAuth;
import com.zipyrar.videojuegosfirebase.R;
import com.zipyrar.videojuegosfirebase.adapters.VideogameAdapter;
import com.zipyrar.videojuegosfirebase.viewmodels.DashboardViewModel;

import java.util.List;

public class DashboardFragment extends Fragment {
    private FirebaseAuth mAuth;
    private DashboardViewModel viewModel;
    private VideogameAdapter adapter;
    private SharedPreferences sharedPref;

    @Nullable
    @Override
    public View onCreateView(@NonNull LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {
        View view = inflater.inflate(R.layout.fragment_dashboard, container, false);

        mAuth = FirebaseAuth.getInstance();
        viewModel = new ViewModelProvider(this).get(DashboardViewModel.class);

        RecyclerView recyclerView = view.findViewById(R.id.recyclerView);
        Button logoutButton = view.findViewById(R.id.btnCierre);
        Button favouritesButton = view.findViewById(R.id.btnFavourites);
        Button themeButton = view.findViewById(R.id.btnThemeMode);

        adapter = new VideogameAdapter(requireContext(), List.of());
        recyclerView.setAdapter(adapter);
        recyclerView.setLayoutManager(new LinearLayoutManager(requireContext()));

        viewModel.getVideogames().observe(getViewLifecycleOwner(), videogames -> {
            if (videogames != null) {
                adapter = new VideogameAdapter(requireContext(), videogames);
                recyclerView.setAdapter(adapter);
            } else {
                Toast.makeText(requireContext(), "Error al cargar datos.", Toast.LENGTH_SHORT).show();
            }
        });

        logoutButton.setOnClickListener(v -> {
            mAuth.signOut();
            Toast.makeText(requireContext(), "Cerraste sesión", Toast.LENGTH_SHORT).show();
            Intent intent = new Intent(requireActivity(), LoginActivity.class);
            startActivity(intent);
            requireActivity().finish();
        });

        favouritesButton.setOnClickListener(v -> {
            Intent intent = new Intent(requireActivity(), FavouritesActivity.class);
            startActivity(intent);
        });

        sharedPref = requireContext().getSharedPreferences("AppConfig", Context.MODE_PRIVATE);
        boolean darkMode = sharedPref.getBoolean("darkMode", false);
        AppCompatDelegate.setDefaultNightMode(darkMode ?
                AppCompatDelegate.MODE_NIGHT_YES : AppCompatDelegate.MODE_NIGHT_NO);

        themeButton.setOnClickListener(v -> {
            boolean isDarkMode = sharedPref.getBoolean("darkMode", false);
            sharedPref.edit().putBoolean("darkMode", !isDarkMode).apply();

            AppCompatDelegate.setDefaultNightMode(isDarkMode ?
                    AppCompatDelegate.MODE_NIGHT_NO : AppCompatDelegate.MODE_NIGHT_YES);

            requireActivity().recreate();
        });

        return view;
    }
}
