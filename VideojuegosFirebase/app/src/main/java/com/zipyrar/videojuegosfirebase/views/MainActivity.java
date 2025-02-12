package com.zipyrar.videojuegosfirebase.views;

import android.app.Dialog;
import android.content.Intent;
import android.os.Bundle;

import androidx.appcompat.app.AppCompatActivity;
import androidx.databinding.DataBindingUtil;
import androidx.fragment.app.Fragment;

import com.google.firebase.auth.FirebaseAuth;
import com.zipyrar.videojuegosfirebase.R;
import com.zipyrar.videojuegosfirebase.databinding.ActivityMainBinding;


public class MainActivity extends AppCompatActivity {
    private ActivityMainBinding binding;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        binding = DataBindingUtil.setContentView(this, R.layout.activity_main);

        binding.navigationView.setNavigationItemSelectedListener(item -> {
            if(item.getItemId()==R.id.nav_dashboard) {
                openFragment(new DashboardFragment());
            } else if(item.getItemId()==R.id.nav_favourites) {
                openFragment(new FavouritesFragment());
            } else if(item.getItemId()==R.id.nav_profile) {
                openFragment(new ProfileFragment());
            } else if(item.getItemId()==R.id.nav_logout) {
                logoutUser();
            }
            binding.drawerLayout.closeDrawers();
            return true;
        });

        if (savedInstanceState == null) {
            openFragment(new DashboardFragment());
        }
    }

    private void openFragment(Fragment fragment) {
        getSupportFragmentManager().beginTransaction()
                .replace(R.id.fragmentContainer, fragment)
                .commit();
    }

    private void logoutUser() {
        FirebaseAuth.getInstance().signOut();
        Intent intent = new Intent(this, LoginActivity.class);
        startActivity(intent);
        finish();
    }
}
