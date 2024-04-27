import { Download } from "lucide-react";
import React from "react";
import { useDropzone } from "react-dropzone";

type DropzoneProps = {
  disabled?: boolean;
  onDrop: any;
  acceptTypes?: any
};

const Dropzone: React.FC<DropzoneProps> = ({onDrop, acceptTypes, disabled}) => {
  const { getRootProps, getInputProps, isDragActive } = useDropzone({
    accept: acceptTypes,
    onDrop: (acceptedFiles) => onDrop(acceptedFiles),
  });

  return (
    <div
      {...getRootProps({ className: "dropzone" })}
      className="dropzone cursor-pointer p-4 flex h-36 w-full flex-col items-center justify-center rounded-md border border-dashed border-gray-300 md:h-64 lg:w-96 md:p-10"
      style={disabled ? {opacity: 0.5, cursor: "auto"} : {}}
    >
      <input {...getInputProps()} disabled={disabled} />
      <Download className="h-8 w-8 md:h-9 md:w-9 text-primary" />
      <div className="text-center">
        {isDragActive ? (
          <p className="text-xs text-muted-foreground pt-3">Перетаскивать сюда сюда ...</p>
        ) : (
          <p className="text-xs text-muted-foreground pt-3">Загрузите файл, нажав сюда или перетащив его</p>
        )}
      </div>
    </div>
  );
};
export default Dropzone;
