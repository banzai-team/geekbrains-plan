/*
  Warnings:

  - Added the required column `source` to the `ModelRequest` table without a default value. This is not possible if the table is not empty.
  - Added the required column `source_type` to the `ModelRequest` table without a default value. This is not possible if the table is not empty.

*/
-- AlterTable
ALTER TABLE "ModelRequest" ADD COLUMN     "source" TEXT NOT NULL,
ADD COLUMN     "source_type" TEXT NOT NULL;
