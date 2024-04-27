/*
  Warnings:

  - Added the required column `difficulty` to the `Program` table without a default value. This is not possible if the table is not empty.

*/
-- AlterTable
ALTER TABLE "Program" ADD COLUMN     "difficulty" TEXT NOT NULL;
