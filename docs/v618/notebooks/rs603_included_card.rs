echo Now reading the included file!;

echo Including datasets in a Workspace in a Root file...;
data1 = import(rs603_infile.root,
               rs603_ws,
               data1);

data2 = import(rs603_infile.root,
               rs603_ws,
               data2);
