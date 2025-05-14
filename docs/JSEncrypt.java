package devtools;

import java.security.PublicKey;
import java.security.KeyFactory;
import java.security.spec.X509EncodedKeySpec;
import javax.crypto.Cipher;
import java.util.Base64;

public class JSEncrypt {
    public static final char b64pad = '=';
    public static final String b64chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";
    public static final String pubkey = "MFwwDQYJKoZIhvcNAQEBBQADSwAwSAJBAIKLqrfJPM9j4n1IqZJKz3H4U7xkYBNsjVEnfwNjkt+69mJGYktiur9Gx03BcIi3NB3igjDPwchpvzwVO9SxVSsCAwEAAQ==";
    public static final String prikey = "MIIBUwIBADANBgkqhkiG9w0BAQEFAASCAT0wggE5AgEAAkEAgouqt8k8z2PifUipkkrPcfhTvGRgE2yNUSd/A2OS37r2YkZiS2K6v0bHTcFwiLc0HeKCMM/ByGm/PBU71LFVKwIDAQABAkAo/PNIKz4Vm7YEQilDzotdrGuWLingT2f7gBwoEz6NUjEKa/pceSnO/hnIkW9z2V6kkjOUlKC1ICbEXnueLbUZAiEA2Nbq0x7mjy9diOaJpUE6gmy5D0ZwGZ/LFODB8WIxkbUCIQCaHyUbfbTPlVYn3TTVNCS3lwARZ7PUYJgMUt/v9IEXXwIgLoeXpiv4T3tbd9f4a2Se2IPaBiQYQ/ddDaLZGyH1/w0CIA6PwsHGLr8uLOW3ULaUJqPx8F+0nJkER1liuyXAxDGhAiBXM1AG2N8Tk+5h6Rc6pWj29eLobrZkAAmBXKKf6+/+kQ==";

    public static void main(String[] args) {
        String text = "tieshan";
        try {
            System.out.println(encrypt(text));
        } catch (Exception e) {
            e.printStackTrace();
        }
        
    }

    public static PublicKey getPublicKey() throws Exception {
        byte[] decodedKey = Base64.getDecoder().decode(pubkey);
        X509EncodedKeySpec spec = new X509EncodedKeySpec(decodedKey);
        KeyFactory kf = KeyFactory.getInstance("RSA");
        return kf.generatePublic(spec);
    }

    public static String encrypt(String text) throws Exception {
        Cipher cipher = Cipher.getInstance("RSA/ECB/PKCS1Padding");
        cipher.init(Cipher.ENCRYPT_MODE, getPublicKey());
        byte[] encrypted = cipher.doFinal(text.getBytes());
        return Base64.getEncoder().encodeToString(encrypted);
    }
}