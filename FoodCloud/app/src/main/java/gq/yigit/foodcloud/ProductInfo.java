package gq.yigit.foodcloud;

import android.content.Intent;
import android.nfc.Tag;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.TextView;
import android.widget.Button;

import com.google.api.client.json.JsonObjectParser;
import com.google.firebase.database.*;
import java.util.HashMap;
import java.util.Map;
import java.util.ArrayList;
import android.view.View.OnClickListener;
import android.widget.Toast;

import org.json.JSONException;
import org.json.JSONObject;

public class ProductInfo extends AppCompatActivity implements OnClickListener {
    private static final String TAG = "MainActivity";
    private TextView Name;
    private TextView Cal;
    private TextView Cooked;
    private TextView Nutrients;
    private TextView BBD;
    private TextView Processed;
    private TextView Problematic;
    private TextView Allergens;
    private String name;
    private String  cal;
    private String cooked;
    private String nutrients;
    private ArrayList nutrients_array;
    private String bbd;
    private String processed;
    private String problematic;
    private String allergens;
    private ArrayList allergens_array;
    public String json_str;
    public JSONObject Prod;
    private Button scanBtn;
    private Button jrnyBtn;
    public String prod_loc;
    public String allergens_print = new String();
    public String nutrients_print = new String();



    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_product_info);

    }

    @Override
    public void onClick(View v){
        if (v.getId() == R.id.button) {
            Intent i = new Intent(ProductInfo.this, MainActivity.class);
            startActivity(i);
        }if (v.getId() == R.id.journey) {
            Intent i = new Intent(ProductInfo.this, LearnMore.class);
            i.putExtra("key", prod_loc);
            startActivity(i);
        }
    }

    public void onStart(){
        super.onStart();
        setContentView(R.layout.activity_product_info);
        Map<String, String> map = new HashMap<String, String>();
        FirebaseDatabase database = FirebaseDatabase.getInstance();
        DatabaseReference myRef = database.getReference();
        scanBtn = (Button)findViewById(R.id.button);
        scanBtn.setOnClickListener(this);
        jrnyBtn = (Button)findViewById(R.id.journey);
        jrnyBtn.setOnClickListener(this);


                Bundle extras = getIntent().getExtras();
                if (extras != null) {
                    prod_loc = extras.getString("key");
                    //The key argument here must match that used in the other activitylgo
                }
                // This method is called once with the initial value and again
                // whenever data at this location is updated.
                PHPComm comm = new PHPComm(this);
                comm.execute("get", "1", "Products");
                try {
                    json_str = comm.json_return;
                    while(json_str == null){
                       json_str = comm.json_return;
                       continue;
                    }

                    Log.d(TAG,"This is a pointer");
                    //Log.d(TAG,"get json str" + json_str);
                    //JSONObject jsonObj = new JSONObject(json_str);
                }catch (NullPointerException e) {
                    Log.d(TAG, "An error occured with the json!");
                }
                /*
                Name = (TextView) findViewById(R.id.name);
                Name.setText( name);
                Cal = (TextView) findViewById(R.id.Calories);
                Cal.setText(cal);
                Allergens = (TextView) findViewById(R.id.allergens);
                allergens_print = "";
                if(allergens.isEmpty()) {
                    Allergens.setText("Allergens : None");
                }else{
                    for(int i = 0; i < allergens.size();i++) {
                        allergens_print = allergens_print + allergens.get(i);
                        if(i != allergens.size() -1){
                            allergens_print = allergens_print + " , ";
                        }
                    }
                    Allergens.setText("Allergens : " + allergens_print);
                }
                Nutrients = (TextView) findViewById(R.id.nutrients);
                nutrients_print = "";
                if(nutrients.isEmpty()) {
                    Nutrients.setText("Nutrients : None");
                }else{
                    for(int i = 0; i < nutrients.size();i++) {
                        nutrients_print = nutrients_print + nutrients.get(i);
                        if(i != nutrients.size() -1){
                            nutrients_print = nutrients_print + " , ";
                        }
                    }
                    Nutrients.setText("Nutrients : " + nutrients_print);
                }

                Cooked = (TextView) findViewById(R.id.cooked);
                Cooked.setText("Cooked : " + cooked);
                BBD = (TextView) findViewById(R.id.BBD);
                BBD.setText(bbd);
                Processed = (TextView) findViewById(R.id.Process);
                Processed.setText("Process : " + processed);
                */
            }










    }

