/*
  Warnings:

  - Added the required column `foo` to the `ModelResponse` table without a default value. This is not possible if the table is not empty.

*/
-- AlterTable
ALTER TABLE "ModelResponse" ADD COLUMN     "foo" INTEGER NOT NULL;
