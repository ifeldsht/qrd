import java.io.*;

public class CNLPParseTreeExtractor {
  public static void main(String[] argv) throws IOException {
    CNLPParseTreeFileProcessor p = new CNLPParseTreeFileProcessor();
    p.processFile("/home/ilya/data/eng_wikipedia_2016_1M/eng_wikipedia_2016_1M-sentences.txt");
  }
}


