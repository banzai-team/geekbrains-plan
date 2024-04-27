/*
  Warnings:

  - You are about to drop the column `request` on the `ModelRequest` table. All the data in the column will be lost.

*/
-- AlterTable
ALTER TABLE "ModelRequest" DROP COLUMN "request",
ALTER COLUMN "source" DROP NOT NULL,
ALTER COLUMN "source_type" DROP NOT NULL;
