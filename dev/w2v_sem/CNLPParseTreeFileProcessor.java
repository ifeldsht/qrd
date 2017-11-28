import java.io.*;
import java.util.*;
import edu.stanford.nlp.io.*;
import edu.stanford.nlp.ling.*;
import edu.stanford.nlp.pipeline.*;
import edu.stanford.nlp.trees.*;
import edu.stanford.nlp.trees.TreeCoreAnnotations.*;
import edu.stanford.nlp.semgraph.*;
import edu.stanford.nlp.ling.CoreAnnotations.*;
import edu.stanford.nlp.util.*;

public class CNLPParseTreeFileProcessor {
  List<SentenceTreeId> sentenceBuffer;
  List<String> wordBuffer;
  int dumpFrequency;
  
  CNLPParseTreeFileProcessor() {
    sentenceBuffer = new ArrayList<>();
    wordBuffer = new ArrayList<>();
    dumpFrequency = 1000;
  }
  
  void dumpBuffers(int dumpId) throws IOException {
    String dumpIdString = Integer.toString(dumpId);
    String sentenceFile = "out/sentences." + dumpIdString + ".txt";
    String wordFile = "out/words." + dumpIdString + ".txt";
    
    BufferedWriter writer = new BufferedWriter(new FileWriter(sentenceFile));
    for(SentenceTreeId s: sentenceBuffer) {
      s.write(writer);
    }
    writer.close();

    writer = new BufferedWriter(new FileWriter(wordFile));
    for(String w: wordBuffer) {
      writer.write(w);
    }
    writer.close();
  }
  
  void processFile(String fileName) throws IOException {
    CNLPParseTreeProcessor p = new CNLPParseTreeProcessor();
        
    File file = new File(fileName); 
        FileReader fileReader = new FileReader(file);
        BufferedReader bufferedReader = new BufferedReader(fileReader);
        String line;
        int counter = 0, dumpId = 0;
        while ((line = bufferedReader.readLine()) != null) {
          String [] s = line.split("\t"); // ???
          String text = s[1], id = s[0];
          List<CoreMap> sentences = p.processText(text);
          for(CoreMap sentence: sentences) {
             Tree tree = sentence.get(TreeAnnotation.class);
             List<String> words = p.splitTree(tree);
             sentenceBuffer.add( new SentenceTreeId(sentence.toString(),tree.toString(),id,counter) );
             for(String w: words) {
               if( w.length() == 0) continue;
               wordBuffer.add(w);
             }
          }
          counter ++;
          if( counter == dumpFrequency ) {
            dumpBuffers(dumpId);
            sentenceBuffer.clear();
            wordBuffer.clear();
            counter = 0;
            dumpId = 0;
            System.out.println("Last saved ID: " + id);
          }
        }
        fileReader.close();
     }
}
