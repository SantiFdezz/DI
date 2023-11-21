package com.example.myothercatalog;

import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.widget.Toast;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.JsonArrayRequest;
import com.android.volley.toolbox.Volley;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.util.ArrayList;
import java.util.List;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        RecyclerView recyclerview = findViewById(R.id.recycler_view);
        List<AnimalData> data = new ArrayList<>();
        Activity activity = this;
        //Aqui inicializamos el JSON y lo parseamos recibiendo On Response y onErrorResponse
        JsonArrayRequest request = new JsonArrayRequest(
                Request.Method.GET,
                "https://raw.githubusercontent.com/SantiFdezz/DI/main/resource/catalog.json",
                null,
                new Response.Listener<JSONArray>(){
                    @Override
                    public void onResponse(JSONArray response){
                        List<AnimalData> allTheAnimals = new ArrayList<>();
                        for (int i = 0; i < response.length(); i++){
                            try{
                                JSONObject animal = response.getJSONObject(i);
                                AnimalData data = new AnimalData(animal);
                                allTheAnimals.add(data);
                            }catch(JSONException e){
                                e.printStackTrace();
                            }
                        }
                        AnimalRecyclerViewAdapter adapter = new AnimalRecyclerViewAdapter(allTheAnimals, activity);
                        recyclerview.setAdapter(adapter);
                        recyclerview.setLayoutManager(new LinearLayoutManager(activity));
                    }
                },
                new Response.ErrorListener(){
                    @Override
                    public void onErrorResponse(VolleyError error){
                        Toast.makeText(activity, error.getMessage(), Toast.LENGTH_SHORT).show();
                    }
                });
        RequestQueue cola = Volley.newRequestQueue(this);
        cola.add(request);
    }

}