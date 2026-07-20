from pathlib import Path
import pandas as pd

class DataLoader:
    
    def validate_path(self,file_path):
        file_path=Path(file_path)
        if not file_path.exists():
            raise FileNotFoundError(f"File not found: {file_path}")
        if not file_path.is_file():
            raise ValueError(f"Expected a file but got a directory: {file_path}")
        if file_path.suffix.lower()!=".csv":
            raise ValueError(f"Expected a .csv file but got {file_path.suffix}")
        return file_path
        
    def load_csv(self,file_path):
        file_path=self.validate_path(file_path)
        return pd.read_csv(file_path)
            
    def save_csv(self,dataframe,output_path):
        output_path = Path(output_path)
        if output_path.suffix.lower()!=".csv":
            raise ValueError("Output file must have a .csv extension")
        output_path.parent.mkdir(parents=True,exist_ok=True)
        dataframe.to_csv(output_path,index=False)
        return output_path