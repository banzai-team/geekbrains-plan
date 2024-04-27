/*
  Warnings:

  - A unique constraint covering the columns `[request_id]` on the table `ModelResponse` will be added. If there are existing duplicate values, this will fail.

*/
-- CreateIndex
CREATE UNIQUE INDEX "ModelResponse_request_id_key" ON "ModelResponse"("request_id");

-- AddForeignKey
ALTER TABLE "ModelResponse" ADD CONSTRAINT "ModelResponse_request_id_fkey" FOREIGN KEY ("request_id") REFERENCES "ModelRequest"("id") ON DELETE CASCADE ON UPDATE CASCADE;
