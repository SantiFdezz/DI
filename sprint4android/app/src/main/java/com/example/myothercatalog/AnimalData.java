package com.example.myothercatalog;

import org.json.JSONException;
import org.json.JSONObject;

public class AnimalData {
    private String name;
    private String description;
    private String imageUrl;
    //Setteamos los datos que vamos a enseñar por cada celda

    //Recogemos los datos
    public AnimalData(JSONObject json){
        try{
            this.name = json.getString("name");
            this.description = json.getString("description");
            this.imageUrl = json.getString("image_url");

        }catch(JSONException e){
            e.printStackTrace();
        }
    }
    public String getName(){ return name;}
    public String getImageUrl(){ return imageUrl;}
    public String getDescription(){ return description;}

}
