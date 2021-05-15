import Data_pipeline
data= Data_pipeline.data_pipeline()
text = """Jobs was raised by adoptive parents in Cupertino, California, located in what is now known as Silicon Valley. Though he was interested in engineering, his passions of youth varied. He dropped out of Reed College, in Portland, Oregon, took a job at Atari Corporation as a video game designer in early 1974, and saved enough money for a pilgrimage to India to experience Buddhism.

Back in Silicon Valley in the autumn of 1974, Jobs reconnected with Stephen Wozniak, a former high school friend who was working for the Hewlett-Packard Company. When Wozniak told Jobs of his progress in designing his own computer logic board, Jobs suggested that they go into business together, which they did after Hewlett-Packard formally turned down Wozniak’s design in 1976. The Apple I, as they called the logic board, was built in the Jobses’ family garage with money they obtained by selling Jobs’s Volkswagen minibus and Wozniak’s programmable calculator.""" 
x =  data.wh_parse_text(text)
print(x)