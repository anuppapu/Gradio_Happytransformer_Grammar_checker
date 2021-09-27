import gradio as gr
from happytransformer import HappyTextToText
from happytransformer import TTSettings

settings = TTSettings(do_sample=True, top_k=10, temperature=0.5,  min_length=1, max_length=100)
happy_tt = HappyTextToText("T5",  "prithivida/grammar_error_correcter_v1")

def correct_text(inp):
  text = "gec: " + inp
  result = happy_tt.generate_text(text, args=settings)
  return result.text

input_text = gr.inputs.Textbox(lines=7,label="Enter Text Here...")
output_text = gr.outputs.Textbox(label="Corrected Sentence")

iface = gr.Interface(fn=correct_text, inputs=input_text, outputs=output_text, title="Grammar Correction Tool", 
             description='This tool can be used to correct the grammar of a Sentence', 
             allow_screenshot=False, allow_flagging=False,layout="vertical",theme="compact")
if __name__ == "__main__":
  iface.launch(inline=None,debug=False,share=False)
