import java.io.*;

public class SentenceTreeId {
  public String sentence;
  public String tree;
  public String id;
  public int counter;
  
  SentenceTreeId(String s, String t, String i, int c) {
    sentence = s;
    tree = t;
    id = i;
    counter = c;
  }
  
  public void write(BufferedWriter writer) throws IOException {
//    writer.write(Integer.toString(counter)+"\n");
    writer.write(id+"\n");
    writer.write(sentence+"\n");
    writer.write(tree+"\n");
  }
}
