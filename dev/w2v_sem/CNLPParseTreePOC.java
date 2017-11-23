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

public class CNLPParseTreePOC {
    public static void main(String [] args) throws IOException {
        CNLPParseTreeProcessor p = new CNLPParseTreeProcessor();
        String text = "Cook is holding knife and cat is looking at milk";
        List<CoreMap> sentences = p.processText(text);
        for(CoreMap sentence: sentences) {
            Tree tree = sentence.get(TreeAnnotation.class);
            System.out.println(sentence);
            System.out.println(tree);
            List<String> words = p.splitTree(tree);
            for(String w: words) {
                System.out.println(w);
            }
        }
    }
}

