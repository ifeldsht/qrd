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

public class CNLPParseTreeProcessor {
    StanfordCoreNLP pipline;
    List<String> buffer;
    
    CNLPParseTreeProcessor() {
        buffer = new ArrayList<>();
        Properties pr = new Properties();
        pr.setProperty("annotators","tokenize,ssplit,pos,lemma,mer,parse");
        pipeline = new StanfordCoreNLP(pr);
    }

    List<CoreMap> processText(String text) {
        Annotatopn annotation = new Annotation(text);
        pipeline.annotate(annotation);
        return annotation.get(SentencesAnnotation.class);
    }

    List<String> splitText(Tree T) {
        buffer.clear();
        fillBuffer(T);
        return buffer;
    }

    void fillBuffer(Tree T) {
        List<LabeledWord> L = T.labeledYield();
        String s = "";
        for(LabeledWord w: L) s += w.word() + " ";
        buffer.add(s);
        for(Tree c: T.getChildrenAsList()) fillBuffer(c);
    }
}

