generate_data_set <- function(vector_of_paths_to_data_files) {
 number_of_paths_to_data_files <- length(vector_of_paths_to_data_files)
 header <- c("ID", "X", "Y", "Map X", "Map Y", "Lat", "Lon", "B1", "B2", "B3", "Class")
 composite_data_frame <- data.frame(matrix(ncol = length(header), nrow = 0))
 colnames(composite_data_frame) <- header
 vector_of_numbers_of_rows <- rep(0, number_of_paths_to_data_files)
 for (i in 1:number_of_paths_to_data_files) {
  data_frame <- read.table(
   file = vector_of_paths_to_data_files[i],
   comment.char = ";"
  )
  number_of_rows <- nrow(data_frame)
  vector_of_classes <- rep("", number_of_rows)
  if (grepl("NON", vector_of_paths_to_data_files[i], fixed = TRUE) | grepl("NOT", vector_of_paths_to_data_files[i], fixed = TRUE)) {
   vector_of_classes <- rep("Not Blue Tarp", number_of_rows)
  } else {
   vector_of_classes <- rep("Blue Tarp", number_of_rows)
  }
  data_frame$Class <- vector_of_classes
  colnames(data_frame) <- header
  composite_data_frame <- rbind(composite_data_frame, data_frame)
  vector_of_numbers_of_rows[i] = nrow(data_frame)
 }
 data_set <- list(
  data_frame = composite_data_frame,
  vector_of_numbers_of_rows = vector_of_numbers_of_rows
 )
 return(data_set)
}