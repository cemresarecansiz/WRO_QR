
/*
PAUSE FOR PRAYER

Dear God,
Please help me find any malicious bugs that I've created
and ,yet, I can't spot.
Make my code free of errors.


END PRAYER
*/

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

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

public class ProductInfo extends AppCompatActivity implements OnClickListener {
    private static final String TAG = "MainActivity";
    static private TextView Name;
    static private TextView Cal;
    static private TextView Cooked;
    static private TextView Nutrients;
    static private TextView BBD;
    static private TextView Processed;
    static private TextView Problematic;
    static private TextView Allergens;
    static private String name;
    static private String  cal;
    static private String cooked;
    static private String nutrients;
    static private JSONArray nutrients_array;
    static private String bbd;
    static private String processed;
    static private String expiry_date;
    static private String allergens;
    static private JSONArray allergens_array;
    public String json_str;
    public JSONObject Prod;
    private Button scanBtn;
    private Button jrnyBtn;
    public String prod_loc;
    static public String allergens_print = new String();
    static public String nutrients_print = new String();



    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_product_info);
        scanBtn = (Button)findViewById(R.id.button);
        scanBtn.setOnClickListener(this);
        jrnyBtn = (Button)findViewById(R.id.journey);
        jrnyBtn.setOnClickListener(this);
        Name = (TextView) findViewById(R.id.name);
        Cal = (TextView) findViewById(R.id.Calories);
        Allergens = (TextView) findViewById(R.id.allergens);
        Cooked = (TextView) findViewById(R.id.cooked);
        BBD = (TextView) findViewById(R.id.BBD);
        Processed = (TextView) findViewById(R.id.Process);
        Bundle extras = getIntent().getExtras();
        if (extras != null) {
            prod_loc = extras.getString("key");
        }

        PHPComm comm = new PHPComm(this);
        comm.execute("get", prod_loc, "Products");


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


            static public void continueApp(String json_str){
                try {
                    Log.d(TAG,"This is a pointer");
                    Log.d(TAG,"Got json str " + json_str);
                    JSONObject jsonObj = new JSONObject(json_str);
                    name = jsonObj.get("Prod_Name").toString();
                    cal = jsonObj.get("Calories").toString();
                    cooked = jsonObj.get("Cooked").toString();
                    nutrients = jsonObj.get("Nutrients").toString();
                    bbd = jsonObj.get("BBD").toString();
                    processed = jsonObj.get("Process").toString();
                    allergens_array = (JSONArray) jsonObj.get("Allergens");
                    nutrients_array = (JSONArray) jsonObj.get("Nutrients");
                    //expiry_date = jsonObj.getJSONArray("ED").toString();
                    allergens = jsonObj.get("Allergens").toString();
                }catch (JSONException e) {
                    Log.d(TAG, "An error occured with the json!");
                }catch (NullPointerException e){
                    Log.d(TAG,"Received null data!");
                }
                Log.d(TAG,allergens);
                if(allergens.length() < 7) {
                    Allergens.setText("None");
                }else{
                    for(int i = 0; i < allergens_array.length();i++) {
                        try {
                            allergens_print = allergens_print + allergens_array.get(i);
                        }catch (JSONException e){
                            Log.d(TAG,"An error occured with json");
                        }
                        if(i != allergens_array.length()-1){
                            allergens_print = allergens_print + " , ";
                        }
                    }
                    Allergens.setText(allergens_print);
                }
                /*
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
*/

                try {
                    Cal.setText(cal);
                    allergens_print = "";
                    Cooked.setText("Cooked : " + cooked);
                    BBD.setText(bbd);
                    Processed.setText("Process : " + processed);
                    Name.setText(name);

                }catch(NullPointerException e){
                    Log.d(TAG,"Failed");
                }
            }








    }
