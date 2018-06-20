package gq.yigit.foodcloud;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.webkit.WebView;

public class GetInfo extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_get_info);
        WebView myWebView = (WebView) findViewById(R.id.info);
        myWebView.loadUrl("https://www.welthungerhilfe.org/our-work/approaches/food-security-standard/");
    }
}
