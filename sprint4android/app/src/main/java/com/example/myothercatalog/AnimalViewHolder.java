package com.example.myothercatalog;

import android.app.Activity;
import android.view.View;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import com.bumptech.glide.Glide;

public class AnimalViewHolder extends RecyclerView.ViewHolder {
    private final TextView textView;
    private final ImageView imageView;

    public AnimalViewHolder(@NonNull View itemView){
        //Creamos el viewHolder e igualamos los datos
        super(itemView);
        textView = (TextView) itemView.findViewById(R.id.animal_name_text_view);
        imageView = (ImageView) itemView.findViewById(R.id.animal_image_view);

    }
    public void showData(AnimalData data, Activity activity){
        //Mostramos los datos
        textView.setText(data.getName());
        Glide.with(itemView.getContext())
                .load(data.getImageUrl())
                .into(imageView);
    }
}
